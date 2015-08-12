(function(global){
    var onCityChange = function(){
        $('#city_input').click(function(){
           ajaxGet('/api/area/taipei_city/', function(content){
               console.log(content);
           });
        });
    };

    onCityChange();
})(this);