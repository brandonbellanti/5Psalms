const token = '1d0167ef5a0d56b0abd7227042d8c92aeb52e251';

fetch('https://api.esv.org/v3/passage/text/?q=Psalm+1', {
  headers: {
    Authorization: `Token ${token}`
  }
}).then(res => res.json()).then(json => console.log(json));