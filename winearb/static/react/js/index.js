import React from 'react';
import ReactDOM from 'react-dom';

import Grid from 'react-bootstrap/lib/Grid';

import { ArticleList } from './article_list.js';
import { Base } from './home.js';

import { CustomJTron } from './articles.js';
import Title from './components/title.js';
import { Services } from './services.js';


const userAuth = document.getElementById("userAuth").value;

try {
    const articleData = JSON.parse(document.getElementById("articleData").value);

    ReactDOM.render(
        <Grid fluid={true}>
            <div>
                <Base userAuth={userAuth}/>
                <ArticleList articles={articleData}/>
            </div>
        </Grid>,
      document.getElementById('root')
    );
}   catch (e) {

        ReactDOM.render(
            <Grid fluid={true}>
                <div>
                    <Base userAuth={userAuth}/>
                    <Services main_title="Modern Email" sub_title="Engage your customers." label="Purchase" link="/payments/subscribe/" />
                    <Services main_title="Web App" sub_title="Be with your customers, always." label="Purchase" link="/payments/subscribe/" />
                </div>
            </Grid>,
          document.getElementById('servicepage')
        );
    } finally {
        ReactDOM.render(
            <Grid fluid={true}>
                <div>
                    <Base userAuth={userAuth}/>
                </div>
            </Grid>,
          document.getElementById('container')
        );
    }
