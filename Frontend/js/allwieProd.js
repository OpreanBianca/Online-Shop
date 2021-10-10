
var products;


const getprod = async () => {
	

  const response = await fetch('http://127.0.0.1:5000/product', {
    method: 'GET',
	mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
	  'Access-Control-Allow-Origin': '*',
	  'Accept': '*/*',
	  'Connection': 'keep-alive',
    }
  });
  
	  products = await response.json();
	  onAllviewLoad();
}

function onAllviewLoad(){
	document.getElementById('allviewDescription').innerHTML = products[3].description;
	document.getElementById('allviewPrice').innerHTML = products[3].price;
	document.getElementById('allviewAmount').innerHTML = "Amount: " + products[3].amount;

}

function onBuyClicked(){
	document.getElementById('allShopCart').innerHTML = parseInt(document.getElementById('allShopCart').innerHTML) + 1;
	document.getElementById('allName').innerHTML = "Name: " + products[3].name;
	document.getElementById('allAmount').innerHTML = "Amount: " + document.getElementById('allShopCart').innerHTML;
}

const onFinishBuy = async () => {
	
const amountBody = {
	"id": products[3].id,
	"new_amount": parseInt(document.getElementById('allShopCart').innerHTML)
};

  const response = await fetch('http://127.0.0.1:5000/product/change_amount', {
    method: 'PUT',
	mode: 'cors',
	body: JSON.stringify(amountBody), // string or object
    headers: {
      'Content-Type': 'application/json',
	  'Access-Control-Allow-Origin': '*',
	  'Accept': '*/*',
	  'Connection': 'keep-alive',
    }
  });
  
	  products = await response.json();
	  onAllviewLoad();
}