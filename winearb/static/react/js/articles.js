import React from 'react';
import ReactDOM from 'react-dom';

import Col from 'react-bootstrap/lib/Col';
import Jumbotron from 'react-bootstrap/lib/Jumbotron';
import Image from 'react-bootstrap/lib/Image';
import Button from 'react-bootstrap/lib/Button';
import ButtonGroup from 'react-bootstrap/lib/ButtonGroup';
import Fade from 'react-bootstrap/lib/Fade';

import Title from "./components/title.js";

import { Username } from "./components/username.js";
import { Date } from "./components/date.js";
import Text from "./components/text.js";
import InnerHTML from "./components/innerhtml.js";


function CustomJTron(ShowWrappedComponent, ToggleWrappedComponent) {
    return class FadeInJumbotronIvory extends React.Component {
            constructor(props) {
                super(props);
                this.state = {isClicked: false};

                this.handleClick = this.handleClick.bind(this);
            }

            handleClick () {
                this.setState(prevState => ({
                    isClicked: !prevState.isClicked
                }));
            }


            render() {
                const isClicked = this.state.isClicked;
                return(
                <Col>
                    <div>
                        <Jumbotron style={{backgroundColor: '#FFFFF0', float: 'center', padding: 'none', border: 'outset black'}}>
                            <div className="JumbotronItem" style={{textAlign: 'center'}}>
                                <div>
                                    <ShowWrappedComponent {...this.props} />
                                </div>
                                    <ButtonGroup vertical block>
                                        <Col md={6} mdOffset={3}>
                                            <Button bsSize="xsmall" onClick={this.handleClick}>
                                                {isClicked ? 'Close' : 'View Content'}
                                            </Button>
                                        </Col>
                                    </ButtonGroup>
                            </div>
                        </Jumbotron>
                    </div>
                    <div>
                        <Fade in={isClicked} unmountOnExit={true} timeout={1000}>
                            <Jumbotron style={{backgroundColor: '#FFFFF0', float: 'center', padding: 'none', border: 'outset black'}}>
                                <div className="JumbotronItem" style={{textAlign: 'center'}}>
                                    <div>
                                        {this.props.children}
                                        <ToggleWrappedComponent {...this.props} />
                                    </div>
                                </div>
                            </Jumbotron>
                        </Fade>
                    </div>
                </Col>
                );
            }
    }
};

const ArticleHeading = (props) => {
            return(
            <div>
                <Image src={props.image} />
                <Title main_title={props.main_title} sub_title={props.sub_title} />
                <Username username={props.author} />
                <Date date={props.date} />
            </div>
            );
};

const Article = CustomJTron(ArticleHeading, InnerHTML);

export { Article, CustomJTron };
