import { InputGroup, FormControl, Button, Card,
  Col, Row, Container } from 'react-bootstrap';
import React, { useState } from 'react';
import {register} from './Client'

import { useNavigate } from "react-router-dom";

const handleChange = (f) => (event) => f(event.target.value)


export default function Register({children}) {

  return (
    <Container>
      <Row style={{height: '100px'}}></Row>
      <Row>
        <Col></Col>
        <Col xs={8}>
          {children}
        </Col>
        <Col></Col>

      </Row>
    </Container>
  )
}
