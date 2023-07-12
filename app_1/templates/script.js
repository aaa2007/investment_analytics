

        function showPage(page){
          
          document.querySelectorAll('.card').forEach(
           div=>{div.style.display ='none';}
           )
           
          document.querySelector(`#${page}`).style.display='block'
        }
      
        document.addEventListener('DOMContentLoaded',function(){
          document.querySelectorAll('.btnx').forEach(button => {
              button.onclick=function(){
              showPage(this.dataset.page);
           }
        });
      });
