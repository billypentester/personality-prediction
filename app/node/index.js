const express = require('express')
const axios = require('axios')
const app = express()
const port = 3000



app.use(express.static('public'))

app.get('/', (req, res) => {

})

app.get('/prediction', async(req, res) => {
    
    const query = req.query;
    
    var data = [];

    for (const [key, value] of Object.entries(query)) {
        data.push(parseInt(value));
    }

    const result = await axios.post('http://localhost:5000/',data)

    const string = result.data.result.toString();

    string.replace(/'/g, '');

    clean = JSON.parse(string);

    console.log(clean)

    res.send(`<ul> <li> <h1> Extroversion :${clean[0].extroversion} </h1> </li> <li> <h1> Neurotic :${clean[0].neurotic} </h1> </li> <li> <h1> Agreeable: ${clean[0].agreeable} </h1> </li> <li> <h1>  Conscientious: ${clean[0].conscientious} </h1> </li> <li> <h1> Open: ${clean[0].open} </h1> </li> <li> <h1> Cluster: ${clean[0].cluster} </h1> </li>  </ul> `)

})



app.listen(port, () => console.log(`Example app listening on port ${port}!`))
