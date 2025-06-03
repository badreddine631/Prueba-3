This dataset contains data gathered during a experiment in which 19 participants completed n-Back test for n 1,2 & 3 and Stroop test for congruent color and text and incongruent color and text. The data contains is conformed by a EEG signals, aswell as events occured during the tests. Every data is contained in .csv files and there are three types of files: EEG signals, n-back test events and Stroop test events. 

The data files are distributed as follows:
/
|- channels.csv
|- NBack
|   |- EEG_ID.csv
|   |- NBack_ID.csv
|- Stroop
    |- EEG_ID.csv
    |- Stroop_ID.csv

NBack folder contains the data recorded during the n-back test (https://en.wikipedia.org/wiki/N-back) and Stroop folder contains the data recorded during the Stroop test (https://en.wikipedia.org/wiki/Stroop_effect). The naming convention is the next: "DATATYPE_ID.csv", where DATATYPE can be EEG, NBack or Stroop; and ID is an identifier for each participant. There is another file named "channels.csv" which have the correspondence between the channels and the electrode positions following the 10-20 system. Bellow is described the columns of each type of .csv file:

EEG files
---------
- Time: The time in seconds in which each sample is captured from the start of the test.

- EEGN(EEG0, EEG1, EEG2...): The electrical potential recorded by the EEG headset.

NBack files
-----------
- Time: The time in seconds in which each sample is captured from the start of the test.

- Event Code:
	1 TEST START
	2 TEST END
	3 PRESSED CORRECT
	4 PRESSED WRONG
	5 NEW NUMBER APPEARED

- Notes: It gives adaptative information depending on the event code.
	o For TEST START and TEST END events, notes represents the n-back level (1 for 1-back, 2 for 2-back, etc.)
	o For NEW NUMBER APPEARED event, the notes field contains the number showed in the screen.
	o The other two events don't have any aditional information included in the notes

Stroop files
------------
- Time: The time in seconds in which each sample is captured from the start of the test.

- Event Code:
	1 TEST START
	2 TEST END
	5 NEW WORD SHOWN

- Written: The text showed by the test.

- Shown: The color of the font in which the text is written. It can be noted that the color written and the color shown values are in different languages, so bellow there is the correspondence between both fields:
	
	Written		Shown
	---------------------
	rojo		red
	azul		blue
	verde		green
	rosa		pink
	amarillo	yellow
	naranja		darkorange

- Match: This field is filled only for event TEST START. "True" means that for the test that starts at that moment the colors written and shown will be the same always, while "False" means that they may or may not be the same.