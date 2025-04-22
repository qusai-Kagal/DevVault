import express from "express";
import axios from "axios";

const app = express();
const port = 3000;

app.use(express.static("public"));
app.set("view engine", "ejs");

app.get("/", async (req, res) => {
    try {
        const response = await axios.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit");
        res.render("index.ejs", { 
            joke: response.data,
        });
    } catch (error) {
        console.log(error);
        res.status(500).send("Something went wrong!");
    }
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});