jest.unmock('../react/js/components/date.js')

import React from 'react';
import { shallow } from 'enzyme';
import { Date } from '../react/js/components/date.js';

describe('Date', () => {
    let wrapper;
    
    beforeEach(() => {
        wrapper = shallow(<Date date={'November 30, 2012'}/>);
    });
    
    it('should exist', () => {
        expect(wrapper).toBeDefined();
    });
    
    it('should render its props in "Date" div tag', () => {
        expect(wrapper.find('div.Date').childAt(0).text()).toEqual('November 30, 2012');
    });
});