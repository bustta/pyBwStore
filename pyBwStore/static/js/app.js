(function(global){
    var initAreaOptions = function(){
        var areaOptniosHtml = '';
        ajaxGet('/api/area/taipei_city/', function(content){
            var areas;
            try {
                areas = JSON.parse(content);
            }
            catch (e){
                areas = undefined;
            }
            Object.keys(areas).forEach(function(key){
                areaOptniosHtml +=
                    '<option value=' + key + '>' + areas[key] + '</option>';
            });
            $('#area-select').empty().append(areaOptniosHtml);
        });

    };
    initAreaOptions();

    //var onCityChange = function(){
    //    $('#city_input').click(function(){
    //       ajaxGet('/api/area/taipei_city/', function(content){
    //           console.log(content);
    //       });
    //    });
    //};
    //
    //onCityChange();
})(this);