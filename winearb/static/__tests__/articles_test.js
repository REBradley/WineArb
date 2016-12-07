jest.unmock('../react/js/articles.js');

import React from 'react';
import ReactDOM from 'react-dom';
import { mount } from 'enzyme';
import { Article } from '../react/js/articles.js';

const TESTDATA = {
  main_title: "Cabernet Sauvignon",
  sub_title: "The Grape You Need to Know",
  author: "Bobby B",
  date: "November 17, 2016",
  image: "http://sr3.wine-searcher.net/images/labels/76/33/chateau-mouton-rothschild-pauillac-france-10197633.jpg",
  text: "Minctur? ti oribus evelibus idit antis prae coriam, quisinv enimentiis"
};

describe('Article', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = mount(<Article text={TESTDATA.text}
                                 main_title={TESTDATA.main_title}
                                 sub_title={TESTDATA.sub_title} />);
    });
    
    it('should exist', () => {
        expect(wrapper).toBeDefined();
    });
    
    it('should have an "Article" div tag', () => {
        expect(wrapper.find(".Article").length).toEqual(1);
    });
    
    it('should have an "ArticleText" div tag', () => {
        expect(wrapper.find(".ArticleText").length).toEqual(1);
    });
    
    it('should render its props in an "ArticleText" div tag', () => {
        expect(wrapper.find(".ArticleText").text()).toEqual(TESTDATA.text);
    });
    
    it('should contain a Title that renders its props, both main_title and sub_title', () => {
        expect(wrapper.find("Title").length).toEqual(1);
        expect(wrapper.find("Title").childAt(0).text()).toEqual(TESTDATA.main_title);
        expect(wrapper.find("Title").childAt(1).text()).toEqual(TESTDATA.sub_title);
    });
});
