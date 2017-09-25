
(function() {
	//"arraybuffer", "blob", "document", "json", and "text",jsonp
window.fget = window.fget || {};
fget.requestURL =
    function(url, responseType, callback, opt_errorStatusCallback) {
  var xhr = new XMLHttpRequest();
  if (responseType == "json")
    // WebKit doesn't handle xhr.responseType = "json" as of Chrome 25.
    xhr.responseType = "text";
  else
    xhr.responseType = responseType;

  xhr.onreadystatechange = function(state) {
    if (xhr.readyState == 4) {
      if (xhr.status == 200) {
        var response =
          responseType == "json" ? JSON.parse(xhr.response) : xhr.response;
        callback(response);
      } else {
        if (opt_errorStatusCallback)
          opt_errorStatusCallback(xhr.status);
      }
    }
  };

  xhr.onerror = function(error) {
    console.log("xhr error:", error);
  };

  xhr.open("GET", url, true);
  xhr.send();
};

// ==========
fget.requestPromise =
function pget(url,responseType) { 
  return new Promise((resolve, reject) => {
    var xhr = new XMLHttpRequest();
    if (responseType == "json")
      xhr.responseType = "text"; //for cross-domine 
    else
      xhr.responseType = responseType;

    xhr.open('GET', url);
    xhr.onload = function() {
      if (xhr.status == 200) {
        resolve(xhr.response);
      }
      else {
        reject(Error(xhr.statusText));
      }
    };

    xhr.onprogress = function(e) {
      if (e.lengthComputable)
      {
        var percentage = Math.round((e.loaded/e.total)*100);
        console.log("progress " + percentage + '%' );
      }
      else 
      {
        console.log("total size is unknown");
      }
    };

    xhr.onerror = function() {
      reject(Error("Network Error"));
    };

    xhr.send();
  });
}




})();