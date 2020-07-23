import React from 'react';

import BadgeDetails from './BadgeDetails';
import PageLoading from '../components/PageLoading';
import PageError from '../components/PageError';
import api from '../api';

class BadgeDetailsContainer extends React.Component {
  state = {
    loading: true,
    error: null,
    data: undefined,
    modalIsOpen: false,/* SE INICIALIZA ESTADO DEL MODAL SI DE ABIERTO/CERRADO */
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = async () => {
    this.setState({ loading: true, error: null });

    try {
      const data = await api.badges.read(this.props.match.params.badgeId);
      this.setState({ loading: false, data: data });
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };
  /* CAMBIA LA FUNCION DEL ESTADO DEL MODAL  SI DE ABIERTO/CERRADO */
  handleOpenModal = e => {
    this.setState({ modalIsOpen: true });
  };

  /* CAMBIA LA FUNCION DEL ESTADO DEL MODAL  SI DE ABIERTO/CERRADO */
  handleCloseModal = e => {
    this.setState({ modalIsOpen: false });
  };

  /* FUNCION ASINCRONA PARA ELIMINAR EL BADGE SELECCIONADO */
  handleDeleteBadge = async e => {
    this.setState({ loading: true, error: null });

    try {
      await api.badges.remove(this.props.match.params.badgeId);
      this.setState({ loading: false });
      /* CON history QUE PROCEDE DE ROUTER SE MANDA REDIRECCIONA EN CASO DE EXITO ELINADO EL BADGE */
      this.props.history.push('/badges');
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };

  render() {
    if (this.state.loading) {
      return <PageLoading />;
    }

    if (this.state.error) {
      return <PageError error={this.state.error} />;
    }

    return (
      <BadgeDetails
        {/* PROPS PARA MANDAR ABRIR/CERRAR EL MODAL Y ELIMINAR */}
        onCloseModal={this.handleCloseModal}
        onOpenModal={this.handleOpenModal}
        {/* PROPS PARA PREGUNTAR SI ESTA ABERTO/CERRADO EL MODAL */}
        modalIsOpen={this.state.modalIsOpen}
        onDeleteBadge={this.handleDeleteBadge}
        {/* SE MANDA LA data QUE ESTA EN EL OBJETO state */}
        badge={this.state.data}
      />
    );
  }
}

export default BadgeDetailsContainer;
