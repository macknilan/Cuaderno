import React from 'react';
import { Link } from 'react-router-dom';

import './styles/BadgeDetails.css';
import confLogo from '../images/platziconf-logo.svg';
import Badge from '../components/Badge';
import DeleteBadgeModal from '../components/DeleteBadgeModal';

function BadgeDetails(props) {
  const badge = props.badge;

  return (
    <div>
      <div className="BadgeDetails__hero">
        <div className="container">
          <div className="row">
            <div className="col-6">
              <img src={confLogo} alt="Logo de la Conferencia" />
            </div>
            <div className="col-6 BadgeDetails__hero-attendant-name">
              <h1>
                {badge.firstName} {badge.lastName}
              </h1>
            </div>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          <div className="col">
            <Badge
              firstName={badge.firstName}
              lastName={badge.lastName}
              email={badge.email}
              twitter={badge.twitter}
              jobTitle={badge.jobTitle}
            />
          </div>
          <div className="col">
            <h2>Actions</h2>
            <div>
              <div>
                <Link
                  className="btn btn-primary mb-4"
                  to={`/badges/${badge.id}/edit`}
                >
                  Edit
                </Link>
              </div>

              <div>
                {/* PRPOS QUE SE ENVIA PARA ABRIR MODAL Y CONFIRMAR ELIMINAR BADGE */}
                <button onClick={props.onOpenModal} className="btn btn-danger">
                  Delete
                </button>
                <DeleteBadgeModal
                  {/* COMPONENTE QUE PRESENTA EL CONTENIDO DE DEL MODAL PARA DECIDIR SI/NO ELIMINAR */}
                  {/* SE MANDAN LOS PROPS "isOpen" "onClose" "onDeleteBadge" */}
                  isOpen={props.modalIsOpen}
                  onClose={props.onCloseModal}
                  onDeleteBadge={props.onDeleteBadge}
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default BadgeDetails;
