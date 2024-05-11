function summarizeVideo(event) {
  var summaryContainer = document.getElementById('summary-container');
  summaryContainer.innerHTML = `<p>Loading...</p>`;
  // create an XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // get the youtube url from the user
  var inputURLField = document.getElementById("youtube-url-input");
  var youtubeUrl = inputURLField.value;

  // open a POST request to the /summarize endpoint
  xhr.open('POST', '/summarize');

  // set the request header
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

  // send the request with the youtube url as the request body
  xhr.send(`youtube_url=${youtubeUrl}`);

  // handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // the request was successful! display the summary
      var summary = xhr.responseText;
      // insert the summary into the HTML
      var summaryContainer2 = document.getElementById('summary-container');
      summaryContainer2.innerHTML = `<p>${summary}</p>`;
    } else {
      // there was an error
      alert('Error: ' + xhr.status);
    }
  };
  event.preventDefault();
}
var form = document.getElementById("youtube-url-form");
form.addEventListener("submit", summarizeVideo);