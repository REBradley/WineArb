import React from 'react';

import Navbar from 'react-bootstrap/lib/Navbar';
import Nav from 'react-bootstrap/lib/Nav';
import NavItem from 'react-bootstrap/lib/NavItem';
import Grid from 'react-bootstrap/lib/Grid';
import Image from 'react-bootstrap/lib/Image';



const Base = (props) => {
        if (props.userAuth === 'false') {
            return (
                <Grid>
                    <div>
                        <Navbar style={{textAlign: 'center', backgroundColor: 'transparent', border: 'None'}}>
                            <Navbar.Header>
                                <div>
                                    <a href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline'}}/></a>
                                </div>
                                <Navbar.Toggle />
                            </Navbar.Header>
                            <Navbar.Collapse>
                                <Nav style={{width: '100%', padding: 'none', display: 'inline-block', float: 'center'}}>
                                    <NavItem eventKey={1} href="/articles/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                                    <NavItem eventKey={2} href="/industry/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>TECHNOLOGY</NavItem>
                                    <NavItem eventKey={3} href="/accounts/signup/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>REGISTER</NavItem>
                                    <NavItem eventKey={4} href="/accounts/login/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>SIGN IN</NavItem>
                                </Nav>
                            </Navbar.Collapse>
                        </Navbar>
                    </div>
                </Grid>
            );
        }
        return (
            <Grid>
                <div>
                    <Navbar style={{textAlign: 'center', backgroundColor: 'transparent', border: 'None'}}>
                        <Navbar.Header>
                            <div>
                                <a href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline'}}/></a>
                            </div>
                            <Navbar.Toggle />
                        </Navbar.Header>
                        <Navbar.Collapse>
                            <Nav style={{width: '100%', padding: 'none', display: 'inline-block', float: 'center'}}>
                                <NavItem eventKey={1} href="/articles/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                                <NavItem eventKey={2} href="/industry/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>TECHNOLOGY</NavItem>
                                <NavItem eventKey={3} href="/payments/" style={{ float: 'none', padding: 'none', display: 'inline-block'}}>ACCOUNT</NavItem>
                                <NavItem eventKey={4} href="/accounts/logout/" style={{ padding: 'none', display: 'inline-block'}}>...SIGN OUT</NavItem>
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>
                </div>
            </Grid>
        );
};

export { Base };
