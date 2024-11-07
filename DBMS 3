#Design and Develop MongoDB Queries using CRUD operations. (Use CRUD operations, SAVE method,
logical operators etc.).

use Customer
db.orderSummary.insertOne({
customer_id:1,
name:"Abhijeet",
age:20,
city:"Pune",
purchase_date: new Date("2024-10-01"),
purchase_amount:1,
purchased_product:"Lenovo Gaming Ideapad"})
db.orderSummary.insertMany([{
    customer_id: 2,
    name: "Gunjan",
    age: 21,
    city: "Mumbai",
    purchase_date: new Date("2024-10-03"),
    purchase_amount: 2,
    purchased_product: "HP Pavilion x360"
  },
  {
    customer_id: 3,
    name: "Nikhil",
    age: 20,
    city: "Pune",
    purchase_date: new Date("2024-10-05"),
    purchase_amount: 1,
    purchased_product: "Apple MacBook Air"
  },
  {
    customer_id: 4,
    name: "Yash",
    age: 20,
    city: "Mumbai",
    purchase_date: new Date("2024-09-28"),
    purchase_amount: 3,
    purchased_product: "Dell Inspiron 15"
  },
  {
    customer_id: 5,
    name: "Rajat",
    age: 20,
    city: "Pune",
    purchase_date: new Date("2024-09-30"),
    purchase_amount: 1,
    purchased_product: "Acer Nitro 5"
  },
  {
    customer_id: 6,
    name: "Pratham",
    age: 21,
    city: "Ahemdabad",
    purchase_date: new Date("2024-10-02"),
    purchase_amount: 1,
    purchased_product: "Asus ROG Zephyrus"
  }])
db.orderSummary.find({purchase_amount : {$gt :1}})
db.orderSummary.updateMany({city:"Mumbai"},{$set:{city:"Pune"}})
db.orderSummary.deleteMany({city:"Ahemdabad"})
db.orderSummary.find({$or:[{age:20},{age:21}]})
