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
	  onAppleLoad();
}

function onAppleLoad(){
	document.getElementById('appleDescription').innerHTML = products[4].description;
	document.getElementById('applePrice').innerHTML = products[4].price;
	document.getElementById('appleAmount').innerHTML = "Amount: " + products[4].amount;

}

function onBuyClicked(){
	document.getElementById('allShopCart').innerHTML = parseInt(document.getElementById('allShopCart').innerHTML) + 1;
	document.getElementById('allName').innerHTML = "Name: " + products[4].name;
	document.getElementById('allAmount').innerHTML = "Amount: " + document.getElementById('allShopCart').innerHTML;
}

const onFinishBuy = async () => {
	
const amountBody = {
	"id": products[4].id,
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
	  onAppleLoad();
}