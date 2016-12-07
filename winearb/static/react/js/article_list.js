import React from 'react';
import ReactDOM from 'react-dom';

import Grid from 'react-bootstrap/lib/Grid';

import { Article } from './articles.js';


function ArticleList(props) {
    const articles = props.articles;

    const list = articles.map((article) =>
            <li key={article.date}><Article
                    main_title={article.main_title}
                    sub_title={article.sub_title}
                    author={article.author}
                    date={article.date}
                    image={article.image.shot}
                    text={article.text} />
            </li>
    );

    return (
        <div className="table">
            <div className="table" style={{ listStyleType: 'none', display: 'inline-block'}} >
               {list}
            </div>
        </div>
    );
}

export { ArticleList };
