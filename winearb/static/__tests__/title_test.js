jest.unmock('../react/js/components/title.js');

import React from 'react';
import ReactDOM from 'react-dom';
import { shallow } from 'enzyme';
import { Title } from '../react/js/components/title.js';


describe('Title', () => {
    let title;
    beforeEach(() => {
        title = shallow(<Title
                        main_title={'Cabernet Sauvignon'}
                        sub_title={'The Grape You Need to Know.'} />);
    })
    
    it('should exist', () => {
        expect(title).toBeDefined();
    });
    
    it('Displays main title in an <h2> element, and subtitle in an <h3> element all wrapped in parent <div>', () => {
        expect(title.type()).toEqual('div');
        expect(title.hasClass('TitleGroup')).toBeTruthy();
        
        let main_title_name = title.childAt(0);
        expect(main_title_name.type()).toEqual('h2');
        expect(main_title_name.hasClass('main_title_text')).toBeTruthy();
        expect(main_title_name.text()).toEqual('Cabernet Sauvignon');
        
        let sub_title_name = title.childAt(1);
        expect(sub_title_name.type()).toEqual('h3');
        expect(sub_title_name.hasClass('sub_title_text')).toBeTruthy();
        expect(sub_title_name.text()).toEqual('The Grape You Need to Know.');
    })
});