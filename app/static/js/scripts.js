// main.js
const spotID = 'a89982e45bc6442a8e5d970a0f5df97b'
const spotSecrete = "d6cbce68078f464f9b0972a40b849377"

const reset = () => {
  event.preventDefault();
  $("#form-user").reset();
}

const validate = () => {
  if($("#first-name").val() == '') {
    alert("Invalid name");
    return false;
  }
  return true;
}

const formatName = (rawInput) => {
  return rawInput.split(' ')[0];
}

const formatGender = (abbr) => {
  return (abbr === 'f') ? 'Female' : 'Male';
}

const appendDiv = (parent, text) => {
  const infoDiv = document.createElement('p');
  infoDiv.innerText = text;
  $(parent).append(infoDiv);
}

const fetchUrl = (url, cb) => {
  fetch(url, {method: 'POST'})
  .then(response=>response.json())
  .then(data=>cb(data))
  .catch((error)=>{alert("Error: " + error)});
}

const getNameInfo = () => {
  console.log("getting name info");
  const nameUrl = 'https://www.behindthename.com/api/lookup.json?key=br715064148'
  if (validate()) {
    console.log("u are Valid");
    let name = formatName($("#first-name").val());
    function cb (data) {
      console.log("in callback");
      let parsed = data[0];
      let text = `First name: ${parsed.name}\n`;
      text += `Gender: ${formatGender(parsed.gender)} \n`;
      let usages = Object.keys(parsed.usages).map(function(k){return parsed.usages[k].usage_full}).join(', ');
      text += `Usages: ${usages}`;
      //appendDiv("#results", text);
      console.log(text);
      //$("#button-advice").show();
      //$("#button-astrol").show();
    }
    console.log('fetching url');
    let full = nameUrl + '&name=' + name; 
    console.log(full);
    fetchUrl(full, cb)
  } else {
    console.log("u are InValid");
  }
}

const getAdvice = () => {
  const adviceUrl = 'https://api.adviceslip.com/advice'
  fetch(adviceUrl, {
      method: 'GET'
  })
  .then(response => response.json())
  .then(data => {
      console.log(data.slip.advice);
//appendDiv("#results", data.slip.advice);
      $("#default-result").text(data.slip.advice);
      $("#results").show();
  });
}

const getHoroscope = () => {
  const aztroUrl = 'https://aztro.sameerkumar.website/?sign=virgo';
  fetch(aztroUrl, {
      method: 'POST'
  })
  .then(response => response.json())
  .then(json => {
      console.log(json);
  });
  /*
  fetch("https://astrology-horoscope.p.rapidapi.com/zodiac_finder/details_requirements/", {
    "method": "GET",
    "headers": {
      "x-rapidapi-key": "83550cd863mshad8f428eb245d0ep1c90bcjsn651da37a03a7",
      "x-rapidapi-host": "astrology-horoscope.p.rapidapi.com"
    }
  })
  .then(response => {
    console.log(response);
  })
  .catch(err => {
    console.error(err);
  });
  */
}

const getCelebs = () => {
  fetch("https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/jason%20bateman", {
    "method": "GET",
    "headers": {
      "x-rapidapi-key": "83550cd863mshad8f428eb245d0ep1c90bcjsn651da37a03a7",
      "x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }
  })
  .then(response => response.json())
  .then(json => {
    json.names.forEach(element => console.log(element));
  })
  .catch(err => {
    console.error(err);
  });
}


$("#button-reset").on('click', reset);
$("#button-advice").on('click', getAdvice);
$("#button-astrol").on('click', getHoroscope);
$("#button-celebs").on('click', getCelebs);

