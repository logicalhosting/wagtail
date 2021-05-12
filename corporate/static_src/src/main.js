import {MDCTopAppBar} from '@material/top-app-bar';
import {MDCCheckbox} from '@material/checkbox';
import {MDCChipSet} from '@material/chips';
import {MDCDataTable} from '@material/data-table';
import {MDCFormField} from '@material/form-field';
import {MDCList} from "@material/list";
import {MDCRadio} from '@material/radio';
import {MDCRipple} from '@material/ripple';
import {MDCTabBar} from '@material/tab-bar';
import {MDCTextField} from '@material/textfield';

const topAppBarElement = document.querySelector('.mdc-top-app-bar');
const topAppBar = new MDCTopAppBar(topAppBarElement);
const dataTable = new MDCDataTable(document.querySelector('.mdc-data-table'));
// const drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
const selector = '.mdc-button, .mdc-icon-button, .mdc-card__primary-action';
const fabRipple = new MDCRipple(document.querySelector('.mdc-fab'));
const tabBar = new MDCTabBar(document.querySelector('.mdc-tab-bar'));
const textField = new MDCTextField(document.querySelector('.mdc-text-field'));

const list = MDCList.attachTo(document.querySelector('.mdc-list'));
list.wrapFocus = true;

const ripples = [].map.call(document.querySelectorAll(selector), function(el) {
  return new MDCRipple(el);
});

const radio = new MDCRadio(document.querySelector('.mdc-radio'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
formField.input = radio;

const checkbox = new MDCCheckbox(document.querySelector('.mdc-checkbox'));
formField.input = checkbox;

const chipSetEl = document.querySelector('.mdc-chip-set');
const chipSet = new MDCChipSet(chipSetEl);