import React from 'react';
import ReactDOM from 'react-dom';

import Grid from 'react-bootstrap/lib/Grid';
import Col from 'react-bootstrap/lib/Col';

import { ArticleList } from './article_list.js';
import { Base } from './home.js';

import { CustomJTron } from './articles.js';
import Title from './components/title.js';
import { Services, WebAppCopy, EmailCopy, ReviewCopy, WineListCopy } from './services.js';


const userAuth = document.getElementById("userAuth").value;

try {
    const articleData = JSON.parse(document.getElementById("articleData").value);

    ReactDOM.render(
        <Grid fluid={true}>
            <Col xs={12} lg={8} lgOffset={2} >
                <Base userAuth={userAuth}/>
                <ArticleList articles={articleData}/>
            </Col>
        </Grid>,
      document.getElementById('root')
    );
}   catch (e) {

        ReactDOM.render(
            <Grid fluid={true}>
                <Col xs={12} lg={8} lgOffset={2} >
                    <Base userAuth={userAuth}/>
                    <Services main_title="Web App" sub_title="Be with your customers, always." label="Purchase" link="/payments/subscribe/">
                        {WebAppCopy}
                    </Services>
                    <Services main_title="Email Marketing" sub_title="Engage your customers." label="Purchase" link="/payments/subscribe/">
                        {EmailCopy}
                    </Services>
                    <Services main_title="Wine List" sub_title="The modern way to sell wine." label="Purchase" link="/payments/subscribe/">
                        {WineListCopy}
                    </Services>
                    <Services main_title="Wine Reviews" sub_title="Remember your wines." label="Free!" link="/reviews/">
                        {ReviewCopy}
                    </Services>
                </Col>
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
