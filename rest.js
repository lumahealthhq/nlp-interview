const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const PORT = process.env.PORT || 8080;

app.listen(PORT, () => console.log('nlp-interview: api interface started on port', PORT));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/getsentiment', (req, res) => {
    if (!req.body.text) {
        return res.json({ error: 'missing text' });
    }
    // do stuff
    res.end();
});