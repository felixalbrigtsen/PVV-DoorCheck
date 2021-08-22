<?php
    $LOGFILE = "data.txt";
    $prevDoorState = true;
    if($_SERVER['REQUEST_METHOD'] === 'POST') {
        $jsonobj = file_get_contents('php://input');
        // $data = json_decode($jsonobj);
        // session_start(); # start session handling.
        // $_SESSION["doorState"] = $data->isDoorOpen;
        // echo $_SESSION["doorState"]; # VIRKER IKKE OM SESSION-VAR IKKE ER SATT

        //TODO - Only store last week, delete old
        $historyFile = fopen($LOGFILE, "a") or die("Unable to open file!");
        fwrite($historyFile, $jsonobj);
        fwrite($historyFile, "\n");
        fclose($historyFile);

        $prevStateFile = fopen($LOGFILE, "w") or die("Unable to open file!");
        fwrite($prevStateFile, $jsonobj);
        fclose($prevDoorState);

        echo "ok";
    
        die();
    } elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
        if (htmlspecialchars($_GET["entries"])) {
            echo readLines(htmlspecialchars($_GET["entries"]));
        } else {            
            echo readLines(1);

        }
    }

    function readLines($lineCount) {
        global $LOGFILE;
        $lines = "";
        $f = fopen($LOGFILE, "r");
        $cursor = -1;

        for ($i = 0; $i < $lineCount; $i++) {
            $line = "";
            fseek($f, $cursor, SEEK_END);
            $char = fgetc($f);

            /**
             * Trim trailing newline chars of the file
             */
            while ($char === "\n" || $char === "\r") {
                fseek($f, --$cursor, SEEK_END);
                $char = fgetc($f);
            }

            /**
             * Read until the start of file or first newline char
             */
            while ($char !== false && $char !== "\n" && $char !== "\r") {
                /**
                 * Prepend the new char
                 */
                $line = $char . $line;
                fseek($f, --$cursor, SEEK_END);
                $char = fgetc($f);
            }
            $lines = $line . "\n" . $lines;
        }

        fclose($f);
        return rtrim($lines, "\n");
      } 


//     - Security?!
// - API for single read
// - API for history
// - Deploy to server
// - Rolling storage, delete old entries

?>
