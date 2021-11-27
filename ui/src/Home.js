import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useNavigate
} from "react-router-dom";
import { InputGroup, FormControl, Button, Card,
  Col, Row, Container } from 'react-bootstrap';

export default function Home() {
  const navigate = useNavigate()
  return (
    <Container>
      <Row style={{height: '100px'}}></Row>
      <Row>
        <Col></Col>
        <Col xs={6}>
          <Card className='md-center'>
            <Card.Body>
              <Button
                className='w-100' variant="primary"
                onClick={()=>navigate('/login')}>Login</Button>
            </Card.Body>
            <Card.Footer>
              <Button
                className='w-100' variant="primary"
                onClick={() => navigate('/register')}>Register</Button>

            </Card.Footer>
          </Card>
        </Col>
        <Col></Col>

      </Row>
    </Container>

 )
}
