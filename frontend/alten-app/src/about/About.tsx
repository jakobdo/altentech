import React from 'react';
import { Card, Table, Row, Col } from 'react-materialize';


function About() {

    return (
        <div className="container">
            <Card>
            <div className="section white">
                <a href="https://www.alten.com/" target="_blank" rel="noopener noreferrer">
                    <img
                        alt="Alten Sweden"
                        src="https://altentechnology.dk/static/base/gfx/alten.sweden.jpg"
                        width="100%"
                    />
                </a>
                <p className="grey-text text-darken-3 lighten-3">
                    ALTEN Group supports the development strategy of its customers in the fields of innovation, R&D and technological information systems.
                    Created 30 years ago in France, the Group has become a world leader in Engineering and Technology consulting.
                    34.000 highly qualified engineers carry out studies and conception projects for the Technical and Information Systems Divisions of major customers in the industrial and service sectors.
                    ALTEN DANMARK A/S works within <b>Energy</b>, <b>Life Science</b>, <b>Banking</b>, <b>Insurance</b> and <b>Robot Industries.</b>
                    </p>
                </div>
                <Row>
                    <Col s={12} m={6}>
                        <Table>
                            <tbody>
                                <tr>
                                    <td></td>
                                    <td></td>
                                </tr>
                                <tr>
                                    <td><strong>Website:</strong></td>
                                    <td><a href="https://www.alten.com/" target="_blank" rel="noopener noreferrer"> ALTEN.com </a></td>
                                </tr>
                                <tr>
                                    <td><strong>Social media:</strong></td>
                                    <td><a href="https://www.linkedin.com/company/alten-danmark/about/" target="_blank" rel="noopener noreferrer"> LinkedIn </a></td>
                                </tr>
                                <tr>
                                    <td><strong>Address:</strong></td>
                                    <td><a href="https://goo.gl/maps/AFAW4SZ9QsACbZF97" target="_blank" rel="noopener noreferrer">Christians Brygge 28<br/> 1559 Copenhagen <br/> Denmark </a></td>
                                </tr>
                            </tbody>
                        </Table>
                    </Col>
                </Row>
            </Card>
            <div>
                <h3>
                    Business Managers
                </h3>
            </div>
            <Card>
                <div className="section white">
                    <Row>
                        <Col s={12} m={4}>
                            <img
                                className="circle responsive-img"
                                src="https://altentechnology.dk/static/base/gfx/katrine.png"
                                alt="Katrine Villumsen"
                            />
                        </Col>
                        <Col s={12} m={6}>
                            <h5>Katrine Villumsen</h5>
                            <Table>
                                <tbody>
                                    <tr>
                                        <td></td>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Social media:</strong></td>
                                        <td><a href="https://www.linkedin.com/in/katrine-villumsen/" target="_blank" rel="noopener noreferrer"> LinkedIn </a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Phone number:</strong></td>
                                        <td><a href="tel:+4541423030">+4541423030</a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Email:</strong></td>
                                        <td><a href="mailto:katrine.villumsen@alten.dk">katrine.villumsen@alten.dk</a></td>
                                    </tr>
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                    <br/>
                    <br/>
                    <Row>
                        <Col s={12} m={4}>
                            <img
                                className="circle responsive-img"
                                src="https://altentechnology.dk/static/base/gfx/nikolaj.png"
                                alt="Nikolaj Enevoldsen"
                            />
                        </Col>
                     
                        <Col s={12} m={6}>
                            <h5>Nikolaj Enevoldsen</h5>
                            <Table>
                                <tbody>
                                    <tr>
                                        <td></td>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Social media:</strong></td>
                                        <td><a href="https://www.linkedin.com/in/nikolajenevoldsen2018/" target="_blank" rel="noopener noreferrer"> LinkedIn </a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Phone number:</strong></td>
                                        <td><a href="tel:+4525529498">+4525529498</a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Email:</strong></td>
                                        <td><a href="mailto:nikolaj.enevoldsen@alten.dk">nikolaj.enevoldsen@alten.dk</a></td>
                                    </tr>
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                </div>
            </Card>
            <div>
                <h3>
                    Human Ressources
                </h3>
            </div>
            <Card>
                <div className="section white">
                    <Row>
                        <Col s={12} m={4}>
                            <img
                                className="circle responsive-img"
                                src="https://altentechnology.dk/static/base/gfx/katja.jpg"
                                alt="Katja Linnea Serritzle"
                            />
                        </Col>
                        <Col s={12} m={6}>
                            <h5>Katja Linnea Serritzlew</h5>
                            <Table>
                                <tbody>
                                    <tr>
                                        <td></td>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Social media:</strong></td>
                                        <td><a href="https://www.linkedin.com/in/katja-linnea-serritzlew/" target="_blank" rel="noopener noreferrer"> LinkedIn </a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Phone number:</strong></td>
                                        <td><a href="tel:+4541300003">+4541300003</a></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Email:</strong></td>
                                        <td><a href="mailto:katja.serritzlew@alten.dk">katja.serritzlew@alten.dk</a></td>
                                    </tr>
                                </tbody>
                            </Table>
                        </Col>
                    </Row>
                </div>
            </Card>
            <div>

            </div>
        </div>
    )
};

export default About;