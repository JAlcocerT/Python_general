<?php

use myPHPNotes\LinkedIn;

require_once "LinkedIn.php";

$app_id = "787k4ec3o5svb9";
$app_secret = "GlYjLOK8AMMLqyfs";
$callback = "http://localhost/callback.php";
$scopes = "r_emailaddress r_basicprofile r_liteprofile";
$ssl = false; //TRUE FOR PRODUCTION ENV.

$linkedin = new LinkedIn($app_id, $app_secret, $callback, $scopes, $ssl);