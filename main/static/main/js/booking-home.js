element = document.querySelector('.edit-database');
elements = document.querySelectorAll('.a-cat');
default_State=0;
element.onclick = function () {
    for (i = 0; i < elements.length; i++) {
        if((elements[i] != element)){
            elements[i].parentElement.classList.toggle("d-none");
        }
    }
    if(default_State==0)
    {
        element.textContent = "Show Categories" 
        default_State =1
    }else{
        element.textContent = "Edit Database"
        default_State=0
    }
    
}