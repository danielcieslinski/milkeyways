import React from 'react';
import { render } from 'react-dom';

import Options from './Options';
import './index.css';

render(
  <Options title={'settings'} />,
//   <Options title={'keys'} />,
  window.document.querySelector('#app-container')
);
