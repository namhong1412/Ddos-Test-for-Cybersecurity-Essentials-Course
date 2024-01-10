<?php

header("Content-Type: text/plain");

function getServerLoad()
{
    if (stristr(PHP_OS, "win")) {
        $cmd = "wmic cpu get loadpercentage /all";
        @exec($cmd, $output);

        foreach ($output as $line) {
            if ($line && preg_match("/^[0-9]+\$/", $line)) {
                return $line;
            }
        }
    } elseif (is_readable("/proc/stat")) {
        $statData1 = _getServerLoadLinuxData();
        sleep(1);
        $statData2 = _getServerLoadLinuxData();

        if (!is_null($statData1) && !is_null($statData2)) {
            $cpuTime = array_sum($statData2) - array_sum($statData1);
            return number_format(100 - ($statData2[3] * 100 / $cpuTime), 2);
        }
    }

    return null;
}

function _getServerLoadLinuxData()
{
    if (is_readable("/proc/stat")) {
        $stats = @file_get_contents("/proc/stat");

        if ($stats !== false) {
            $stats = preg_replace("/[[:blank:]]+/", " ", $stats);
            $stats = explode("\n", str_replace(array("\r\n", "\n\r", "\r"), "\n", $stats));

            foreach ($stats as $statLine) {
                $statLineData = explode(" ", trim($statLine));

                if (count($statLineData) >= 5 && $statLineData[0] == "cpu") {
                    return array_slice($statLineData, 1, 4);
                }
            }
        }
    }

    return null;
}

$cpuLoad = getServerLoad();
echo is_null($cpuLoad) ? "CPU load not estimable" : "$cpuLoad%";

?>
