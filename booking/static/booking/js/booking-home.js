element = document.querySelector(".edit-database");
elements = document.querySelectorAll(".a-cat");
default_State = 0;

if (element) {
  element.onclick = function () {
    for (i = 0; i < elements.length; i++) {
      if (elements[i] != element) {
        elements[i].parentElement.classList.toggle("hidden-toggler");
      }
    }
    if (default_State == 0) {
      element.textContent = "Show Categories";
      default_State = 1;
    } else {
      element.textContent = "Edit Database";
      default_State = 0;
    }
  };
}

/******* filter using categories *******/
category = document.URL.split("=")[1];
if (category) {
  targettedClass = ".category" + category + " a";
  selectedElement = document.querySelector(targettedClass);
  document.querySelector("#categoryHolder").value = category;
}
if (category) {
  selectedElement.parentElement.classList.add("selected")
  selectedElement.href = "?"
}

//categories=document.querySelectorAll(".list-group-item.list-group-item-light a")

// for (i = 0; i < categories.length; i++) {
//     categories[i].onclick = toggleSelection;
// }
// function toggleSelection(){

// }

