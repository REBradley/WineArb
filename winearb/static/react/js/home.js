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
                        <div>
                            <a href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline'}}/></a>
                        </div>
                            <Nav style={{width: '75%', padding: 'none', display: 'inline-block', float: 'center'}}>
                                <NavItem eventKey={1} href="/industry/" style={{float: 'center', padding: 'none', display: 'inline-block'}}>MARKETING</NavItem>
                                <NavItem eventKey={2} href="/articles/" style={{float: 'left', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                                <NavItem eventKey={3} href="/accounts/signup/" style={{float: 'right', padding: 'none', display: 'inline-block'}}>REGISTER</NavItem>
                            </Nav>
                        </Navbar>
                    </div>
                </Grid>
            );
        }
        return (
            <Grid>
                <div>
                    <Navbar style={{textAlign: 'center', backgroundColor: 'transparent', border: 'None'}}>
                    <div>
                        <a href="/articles/"><Image responsive src="/static/images/VIN-ARB.gif" alt="VinArb" style={{display: 'inline'}}/></a>
                    </div>
                        <Nav style={{width: '100%', padding: 'none', display: 'inline-block', float: 'center'}}>
                            <NavItem eventKey={1} href="/industry/" style={{float: 'right', padding: 'none', display: 'inline-block'}}>MARKETING</NavItem>
                            <NavItem eventKey={2} href="/articles/" style={{float: 'left', padding: 'none', display: 'inline-block'}}>HOME</NavItem>
                            <NavItem eventKey={3} href="/payments/" style={{float: 'center', padding: 'none', display: 'inline-block'}}>ACCOUNT</NavItem>
                            <NavItem eventKey={4} href="/reviews/" style={{float: 'center', padding: 'none', display: 'inline-block'}}>REVIEWS</NavItem>
                        </Nav>
                    </Navbar>
                </div>
            </Grid>
        );
};

export { Base };
