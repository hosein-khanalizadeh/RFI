<?php
	$page = isset($_GET['p']) ? $_GET['p'] : '';
	if($page != '')
		include $page;
?>