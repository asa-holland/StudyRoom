import * as functions from 'firebase-functions';


// copied code from https://fireship.io/lessons/how-to-build-a-slack-bot/

export const myBot = functions.https.onRequest( (req,res) => {

    // Request from slack
    const { challenge } = req.body;

    // Response from us
    res.send({ challenge });

   });