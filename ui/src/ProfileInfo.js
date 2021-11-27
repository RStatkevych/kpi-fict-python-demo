import {Card} from 'react-bootstrap'

export default function ProfileInfo({userData}) {
  return <Card>
    <Card.Header>Profile info</Card.Header>
    <Card.Body>
      <p>id: {userData.id}</p>
      <p>Email: {userData.email}</p>
      <p>Name: {userData.name}</p>

    </Card.Body>
  </Card>
}
