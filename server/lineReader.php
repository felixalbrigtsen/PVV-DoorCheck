<?php

function readLines($fname, $lineCount) {
$lines = "";
$f = fopen($fname, "r");
$cursor = -1;

for ($i = 0; $i < $lineCount; $i++) {
    $line = "";
    fseek($f, $cursor, SEEK_END);
    $char = fgetc($f);

    
    //Trim trailing newline chars of the file
    while ($char === "\n" || $char === "\r") {
        fseek($f, --$cursor, SEEK_END);
        $char = fgetc($f);
    }

    //Read until the start of file or first newline char 
    while ($char !== false && $char !== "\n" && $char !== "\r") {
        //Prepend the new char
        $line = $char . $line;
        fseek($f, --$cursor, SEEK_END);
        $char = fgetc($f);
    }
    $lines = $line . "\n" . $lines;
}

fclose($f);
return rtrim($lines, "\n");
} 

?>