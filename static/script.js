document.getElementById("itemForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let phoneNo = document.getElementById("phone_no").value;
    
    fetch("/add_item", {
        method: "POST",
        body: JSON.stringify({ phone_no: phoneNo }),
        headers: { "Content-Type": "application/json" }
    }).then(response => response.json())
      .then(data => console.log(data));
});
