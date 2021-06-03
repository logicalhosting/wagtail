import mdcAutoInit from '@material/auto-init';
import {MDCTopAppBar} from '@material/top-app-bar';
import {MDCDrawer} from "@material/drawer";
import {MDCCheckbox} from '@material/checkbox';
import {MDCChipSet} from '@material/chips/chip-set';
import {MDCFormField} from '@material/form-field';
import {MDCList} from "@material/list";
import {MDCRadio} from '@material/radio';
import {MDCRipple} from '@material/ripple';
import {MDCTextField} from '@material/textfield';
import {MDCDataTable} from '@material/data-table';

const selector = '.mdc-button, .mdc-icon-button, .mdc-card__primary-action';
const ripples = [].map.call(document.querySelectorAll(selector), function(el) {
  return new MDCRipple(el);
});

const topAppBarElement = document.querySelector('.mdc-top-app-bar');
const topAppBar = new MDCTopAppBar(topAppBarElement);
const drawer = new MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));

topAppBar.listen('MDCTopAppBar:nav', () => {
  drawer.open = !drawer.open;
});

const radio = new MDCRadio(document.querySelector('.mdc-radio'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
formField.input = radio;

const checkbox = new MDCCheckbox(document.querySelector('.mdc-checkbox'));
formField.input = checkbox;

const chipSetEl = '.mdc-chip-set'; 
const chipSet = [].map.call(document.querySelectorAll(chipSetEl), function(el) {
  return new MDCChipSet(el);
});

const list = MDCList.attachTo(document.querySelector('.mdc-list'));
list.wrapFocus = true;

const textFieldEl = '.mdc-text-field'; 
const textField = [].map.call(document.querySelectorAll(textFieldEl), function(el) {
  return new MDCTextField(el);
});

const dataTable = new MDCDataTable(document.querySelector('.mdc-data-table'));
