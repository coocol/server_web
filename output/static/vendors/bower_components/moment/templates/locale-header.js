(function (global, factory) {
   typeof exports === 'object' && typeof module !== 'undefined' ? factory(require('static/vendors/bower_components/moment/moment.js')) :
   typeof define === 'function' && define.amd ? define(['moment'], factory) :
   factory(global.moment)
}(this, function (moment) { 'use strict';
