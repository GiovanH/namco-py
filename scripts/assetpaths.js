define([
],
function(
){
    'use strict';  

    var loginUrl = 'http://namcohigh.shiftylook.com/users/login';
    var imageRoot = 'images/',
        styleRoot = 'styles/',
        audioRoot = 'audio/',
        scriptRoot = 'scripts/',
        sceneRoot = 'scripts/namcohigh/scenes/';
    
    var getSceneXMLUrl = function getSceneUrl(sceneName) {
        return sceneRoot+sceneName+'.xml'
    }

    return {
        imageRoot : imageRoot,
        styleRoot : styleRoot,
        audioRoot : audioRoot,
        scriptRoot: scriptRoot,
        sceneRoot : sceneRoot,
        getSceneXMLUrl: getSceneXMLUrl,
        loginUrl: loginUrl
    }

});