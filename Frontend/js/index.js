var userData;

document.getElementById('userImage').style.display = "none";
document.getElementById('userName').style.display = "none";

var cartQuantity = 0;
document.getElementById('cartQuantity').innerHTML = cartQuantity;
cartQuantity

const userLogin = async () => {
	
const loginBody = {
	"email": document.getElementById('userNameInput').value,
	"password": document.getElementById('passwordInput').value
};

  const response = await fetch('http://127.0.0.1:5000/user/login', {
    method: 'POST',
    body: JSON.stringify(loginBody), // string or object
	mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
	  'Access-Control-Allow-Origin': '*',
	  'Accept': '*/*',
	  'Connection': 'keep-alive',
	  
    }
  });
  
  if(response.status === 401){
	document.getElementById('wrongPassword').innerHTML = "Wrong password";
  }
  else{
	  userData = await response.json()
	  document.getElementById('wrongPassword').innerHTML = "Success";
	  document.getElementById('userImage').style.display = "block";
	  document.getElementById('userName').style.display = "block";
	  document.getElementById('loginText').style.display = "none";
	  document.getElementById('userNameText').innerHTML = userData["username"];
	  document.getElementById('userDataUserName').innerHTML = "Username: " + userData["username"];
	  document.getElementById('userDataEmail').innerHTML = "Email: " + userData["email"];
  }
}

function signOut() {
	userData = undefined;
	document.getElementById('userImage').style.display = "none";
	  document.getElementById('userName').style.display = "none";
	  document.getElementById('loginText').style.display = "block";
}
