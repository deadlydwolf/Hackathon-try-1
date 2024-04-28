import express from "express";
import bodyParser from "body-parser";

const port= 3000;
const app=express();

app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static("public"));

import pg from "pg";
const db=new pg.Client({
  user:"postgres",
  host:"localhost",    
  database:"World",
  password:"hallucination7925013",
  port:5432,
});

app.get("/",(req,res)=>{
    res.render("index.ejs")
})

app.get("/login",(req,res)=>{
    res.render("login.ejs")
})

app.post("/submit",(req,res)=>{
    const { name, phone, email, password } = req.body;
    const newUser = [name, phone, email, password];
  
    const sql = 'INSERT INTO users (name, phone, email, password) VALUES ($1, $2, $3, $4)';
    pool.query(sql, newUser, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Error registering user');
      } else {
        console.log('User registered:', result);
        res.status(200).send('User registered successfully');
    }
    
    }
    )
});

app.listen(port,()=>{
    console.log(`Server is runnning on ${port}`);
})