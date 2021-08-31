<?php
    $LOGFILE = "data.txt";
    include "lineReader.php";

    $prevDoorState = true;
    if($_SERVER['REQUEST_METHOD'] === 'POST') {
        $jsonobj = file_get_contents('php://input');

        $historyFile = fopen($LOGFILE, "a") or die("Unable to open file!");
        fwrite($historyFile, $jsonobj);
        fwrite($historyFile, "\n");
        fclose($historyFile);

        echo "ok";
    
        die();
    } elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
        if (htmlspecialchars($_GET["entries"])) {
            echo readLines($LOGFILE, htmlspecialchars($_GET["entries"]));
        } else {            
            echo readLines($LOGFILE, 1);

        }
    }

    
//TODO: Rolling storage, delete old entries?
?>
