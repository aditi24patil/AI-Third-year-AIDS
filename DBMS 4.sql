--Mongo db quries for aggregate functions

var mapFunction = function(){
  emit(this.age,this.purchase_amount);
};

var reduceFunction = function(key,values){
  return Array.sum(values);
};
db.orderSummary.mapReduce(mapFunction,reduceFunction,{out:"Purchase_by_age"})
db.Purchase_by_age.find()
db.orderSummary.aggregate([{$group:{_id:"$age",totalPurchaseAmount:{$sum:"$purchase_amount"}}}])
db.orderSummary.createIndex({age:1})
