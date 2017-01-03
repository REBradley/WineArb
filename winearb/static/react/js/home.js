import React from 'react';

import Navbar from 'react-bootstrap/lib/Navbar';
import Nav from 'react-bootstrap/lib/Nav';
import NavItem from 'react-bootstrap/lib/NavItem';
import Grid from 'react-bootstrap/lib/Grid';
import Col from 'react-bootstrap/lib/Col';
import Image from 'react-bootstrap/lib/Image';



const Base = (props) => {
        if (props.userAuth === 'false') {
            return (
                <Grid fluid={true}>
                    <Col xs={12}>
                        <Navbar fluid={true} style={{textAlign: 'center', backgroundColor: 'transparent', border: 'None' }}>
                            <Navbar.Header style={{ float: 'none' }}>
                                <Navbar.Brand style={{ padding: 'none' }}>
                                    <a style={{ padding: 'none !important' }} href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline-block', float: 'none', padding: 'none'}}/></a>
                                </Navbar.Brand>
                                <Navbar.Toggle style={{ borderColor: '#000000', border: 'none', float: 'center', margin: 'none'}} />
                            </Navbar.Header>
                            <Navbar.Collapse>
                                <Nav style={{width: '100%', padding: 'none', display: 'inline-block', float: 'center'}}>
                                    <NavItem eventKey={1} href="/articles/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                                    <NavItem eventKey={2} href="/industry/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>TECHNOLOGY</NavItem>
                                    <NavItem eventKey={3} href="/reviews/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>REVIEWS</NavItem>
                                    <NavItem eventKey={4} href="/accounts/signup/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>REGISTER</NavItem>
                                    <NavItem eventKey={5} href="/accounts/login/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>SIGN IN</NavItem>
                                </Nav>
                            </Navbar.Collapse>
                        </Navbar>
                    </Col>
                </Grid>
            );
        }
        return (
            <Grid fluid={true}>
                <Col xs={12}>
                    <Navbar fluid={true} style={{textAlign: 'center', backgroundColor: 'transparent', border: 'None'}}>
                        <Navbar.Header style={{ float: 'none' }}>
                            <Navbar.Brand style={{ padding: 'none' }}>
                                <a style={{ padding: 'none !important' }} href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline-block', float: 'none', padding: 'none'}}/></a>
                            </Navbar.Brand>
                            <Navbar.Toggle style={{ borderColor: '#000000', border: 'none', float: 'center', margin: 'none'}} />
                        </Navbar.Header>
                        <Navbar.Collapse>
                            <Nav style={{width: '100%', padding: 'none', display: 'inline-block', float: 'center'}}>
                                <NavItem eventKey={1} href="/articles/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                                <NavItem eventKey={2} href="/industry/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>TECHNOLOGY</NavItem>
                                <NavItem eventKey={3} href="/reviews/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>REVIEWS</NavItem>
                                <NavItem eventKey={4} href="/payments/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>ACCOUNT</NavItem>
                                <NavItem eventKey={5} href="/accounts/logout/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>...SIGN OUT</NavItem>
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>
                </Col>
            </Grid>
        );
};

export { Base };
