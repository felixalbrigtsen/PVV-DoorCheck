<?php 
    //---- DOOR SENSOR ----
    $LOGFILE = "data.txt"; //Filename to read from
    include "lineReader.php"; //Define readLines()
    $prevEntry = json_decode(readLines($LOGFILE, 1));
    $isDoorOpen = $prevEntry->isDoorOpen;
    $prevTime = date("H:i d-m", $prevEntry->time)
    //---- /DOOR SENSOR ----
?>



<style>
/* DOOR SENSOR */
#doorIndicator {
    border-radius: 5px;
    box-shadow: -10px 10px 10px lightgray;
    padding: 8px 8px;
    margin: 4px 4px;
    font-family: monospace;
    font-size: 18px;
}
#doorIndicator > p { display: inline; }
.doorIndicator_OPEN { border: 2px solid green; }
.doorIndicator_CLOSED { border: 2px dotted red; }
/* /DOOR SENSOR */
</style>



<div id="doorIndicator" class="<?php echo($isDoorOpen ? "doorIndicator_OPEN" : "doorIndicator_CLOSED"); ?>">
    <p class="doorStateText">Døren er <b><?php echo($isDoorOpen ? "" : "ikke") ?> åpen</b>.</p>
    <p class="doorStateTime">(Oppdatert <?php echo($prevTime) ?>)</p>
</div>