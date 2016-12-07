import React from 'react';
import ReactDOM from 'react-dom';

import Jumbotron from 'react-bootstrap/lib/Jumbotron';
import Image from 'react-bootstrap/lib/Image';
import Button from 'react-bootstrap/lib/Button';
import ButtonGroup from 'react-bootstrap/lib/ButtonGroup';
import Fade from 'react-bootstrap/lib/Fade';

import Title from "./components/title.js";

import { Username } from "./components/username.js";
import { Date } from "./components/date.js";
import Text from "./components/text.js";


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
                <div>
                    <div>
                        <Jumbotron style={{backgroundColor: '#FFFFF0', float: 'center', padding: 'none', border: 'outset black'}}>
                            <div className="JumbotronItem" style={{textAlign: 'center'}}>
                                <div>
                                    <ShowWrappedComponent {...this.props} />
                                </div>
                                <ButtonGroup vertical block>
                                    <Button bsSize="xsmall" onClick={this.handleClick}>
                                        {isClicked ? 'See Below, Close Here After Viewing' : 'View Content'}
                                    </Button>
                                </ButtonGroup>
                            </div>
                        </Jumbotron>
                    </div>
                    <div>
                        <Fade in={isClicked} unmountOnExit={true} timeout={1000}>
                            <Jumbotron style={{backgroundColor: '#FFFFF0', float: 'center', padding: 'none', border: 'outset black'}}>
                                <div className="JumbotronItem" style={{textAlign: 'center'}}>
                                    <div>
                                       <ToggleWrappedComponent {...this.props} />
                                    </div>
                                </div>
                            </Jumbotron>
                        </Fade>
                    </div>
                </div>
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

const Article = CustomJTron(ArticleHeading, Text);

export { Article, CustomJTron };
