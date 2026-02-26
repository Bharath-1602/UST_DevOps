package ust.springboot.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ust.springboot.entity.Product;

public interface ProductRepository extends JpaRepository<Product, Long> {
}