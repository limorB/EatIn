# EatIn
Peer-To-Peer food delivery app.
the app is meant for people to be able to buy and sell their home cooking dishes.
currently there is no real payment system.
use requirement.txt for dependencies 
cart items - each item added to the cart will receive an id. when a cart item is added to the db it will also receive a NULL value as an order_id. once the user (eater) will proceed to checkout the NULL value will be overridden and all cart items belong to the same cart will receive the same (numeric) order_id.
